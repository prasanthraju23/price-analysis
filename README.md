When considering a product, it’s not enough to know that it’s good; we must also assess the fairness of its current price. To do this, historical pricing data from various vendors can be analyzed. This data can then be used to calculate the Fairness score of the product at the given moment.

A sample equation that can be used to calculate the Goodness score could be of the form:

if Average Price > Current Price:
               fairness = 50+(pavg-pcur)*50/(pavg-pmin)

Else if Average price <=Current Price:
               fairness = 50-(pcur-pavg)*50/(pmax-pavg)
      
The higher the price fairness score, the fairer the current price of the product is considered to be. By taking a Weighted average of both the goodness score and the price fairness score out of 100, a comprehensive score can be determined that indicates the tendency the buyer has to maintain for making the purchase of the given moment.
