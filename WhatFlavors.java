static void whatFlavors(int[] cost, int money) {
        Map<Integer,Integer> prices = new HashMap<>();
        for(int i=0;i<cost.length;i++){
            Integer complement = new Integer((money - cost[i]));
            if(prices.containsKey(complement)){
                System.out.println((prices.get(complement)+1)+" "+(i+1));
            }
            prices.put(cost[i],i);
        }
}
