# Risk
Risk related to potential for downside outcomes
- consequence
- likelihood

## price simulation
Price simulations needed for
- Value at Risk (forward prices)
- Gross Margins at Risk (spot prices)
- Credit at Risk (settlements and MtM)

## simulation methodologies
electricity splot price
- historical sampling + scaling
- structure modeling with bid stack
- stochastic models (mean reverting jump defussion)

electricity forward price (swap or cap)
- historical sampling of returns
- stochastic models (brownian motion)

electricity future price
- combination of spot and forward prices

non-standard contract price
- option pricing model
- equation from forward pricing

LGC and STC price
- historical sampling of returns
- stochastic models (brownian motion)
- other

load simulation
- long term (customer churn) and short term (daily/seasonal shape, flex)
- stochastic expression (ornstein-uhlenbeck)
- regression approach (average of load + rand)
- historical sampling
