# Linear Regression - Project Exercise

Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.

The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out!

## Data

We'll work with the Ecommerce Customers csv file from the company. It has Customer info, suchas Email, Address, and their color Avatar. Then it also has numerical value columns:

* Avg. Session Length: Average session of in-store style advice sessions.
* Time on App: Average time spent on App in minutes
* Time on Website: Average time spent on Website in minutes
* Length of Membership: How many years the customer has been a member. 

Based on the above mentioned features we have to predict the label `Yearly Amount Spent` to help company decide whether to focus on App or Website.


## Inference

### Coeffecients

                    ** Coeficients **
Avg. Session Length     25.981550
Time on App             38.590159
Time on Website          0.190405
Length of Membership    61.279097


Looking at the coefecients for "Time on App (38.590159)" and for "Time on 
website(0.190405)" it is observed that with every minute spent on App would 
increase the "Yearly Amount Spent" by $39 approx where as every minute 
spent on webseite would increase the "Yearly Amount Spent" by $0.19 keeping
other coeffecints fixed. This can be interpreted in two ways :- 
    
 1.) Company can focus more on the website to enhance the user experience 
     on website so that website traffic could be increased, which would
     increase the "Yearly Amount Spent".
    
        
 2.) Company's App is doing much better than the website, Company could 
     focus more on enhancing user experience on App.
