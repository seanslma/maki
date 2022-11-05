# json

The data contract class must have the same name as in the json results for custom datetime conversion:

```c#
using System.Net.Http;
using System.Net.Http.Headers;
using Newtonsoft.Json;

public class MyRes 
{
    HttpClient _sol;

    public MyRes()
    {
        var hdl = new HttpClientHandler() { UseDefaultCredentials = true };
        _sol = new HttpClient(hdl);
        _sol.Timeout = TimeSpan.FromMinutes(Config.ApiTimeout);
        _sol.BaseAddress = new Uri(Config.ApiBase + "/");
        _sol.DefaultRequestHeaders.Accept.Clear();

        //add an accept header for JSON format
        _sol.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
    }
    
    public List<ResInfo> GetResList(string urn)
    {
        var res = _sol.GetAsync(urn).Result;
        if (res.IsSuccessStatusCode) {
            //simple
            //return res.Content.ReadAsAsync<List<ResInfo>>().Result;
            //with custom date converter
            string jsonContent = res.Content.ReadAsStringAsync().Result;
            return JsonConvert.DeserializeObject<List<ResInfo>>(jsonContent);
        }
        else {
            Log.Err($"Connection failed. Status Code: {res.StatusCode}. Reason Phrase: {res.ReasonPhrase}\n  url: {_baseAddress + urn}");
        }
        return new List<ResInfo>();
    }
            
    /*
    [{ResID:1, ResName:"John", ResDate:"2021-09-01T12:09:08"},{...}]
    */
    [DataContract]
    public class ResInfo
    {
        [DataMember(Order = 1)] public string ResID { get; set; }
        [DataMember(Order = 2)] public string ResName { get; set; }
        [JsonConverter(typeof(CustomDateTimeConverter))]
        [DataMember(Order = 3)] public DateTime ResDate { get; set; }
    }
}

public class CustomDateTimeConverter : Newtonsoft.Json.Converters.IsoDateTimeConverter
{
    public CustomDateTimeConverter()
    {
        base.DateTimeFormat = "yyyy-MM-ddTHH:mm:ss";
    }
}
```
