#CLI

```c#
class CliParam
{
	string _dir;
	public string Dir =>_dir; 

	DateTime _date;
	public DateTime Date => _date;

	public int ParseParam(string[] args)
	{
		int ret = 0;

		List<string> pars;
		Dictionary<string, List<string>> clipars;
		ret = CliArgs(args, out clipars);

		//dir
		if (clipars.TryGetValue("-dir", out pars) && par.Count > 0) {
			_dir = pars[0].Trim();
			if (string.IsNullOrEmpty(_dir)) {
				return Log.Err($"'-dir' parameter is not a directory");
			}
		}
		else {
			return Log.Err($"'-dir' parameter is required but not provided");
		}

		//date
		if (clipars.TryGetValue("-date", out pars) && par.Count > 0) {
			var par = pars[0].Trim();
			if (string.IsNullOrEmpty(par)) {
				_date = DateTime.MinValue;
			}
			else {
				_date = DateTime.ParseExact(par, "yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture);
			}
		}
		else {
			_date = DateTime.MinValue;
		}

		return ret;
	}

	int CliArgs(string[] args, out Dictionary<string, List<string>> clipars)
	{
		int ret = 0;
		cli = null;

		int i = 0;
		int n = args.Length;
		clipars = new Dictionary<string, List<string>>();
		while (i < n) {
			if (args[i][0] != '-') {
				return Log.Err($"Arg '{args[i]}' unexpected - should be an -option?");
			}

			var opt = args[i];
			var pars = new List<string>();
			while (++i != n) {
				if (args[i].Length > 0 && args[i][0] == '-')
					break;
				pars.Add(args[i]);
			}
			clipars[opt] = pars;
		}
		return ret;
	}
}
```
