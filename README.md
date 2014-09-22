## Hipchat Visualizations

This is a tool to produce a simple webpage to display hipchat logs.

It isn't intended to be particularly useful or insightful, but it looks pretty cool.

To run this locally, create the file ~/.hypchat, and fill it with

```
[HipChat]
token = YourHipchatApiToken
roomId = 12345
```

Then, run 

```pip install hypchat```

You may need to modify your version of HypChat, as it requires [this pull request](https://github.com/RidersDiscountCom/HypChat/pull/14). If it is not yet merged, you should be able to manually make those changes.