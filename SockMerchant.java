static int sockMerchant(int n, int[] ar) {
        int c=0;
        HashSet<Integer> h = new HashSet<Integer>();
        h.add(ar[0]);
        for(int i=1; i<ar.length;i++){
            System.out.println(ar[i]);
            if(h.contains(ar[i])){
                c++;
                h.remove(ar[i]);
            }else{
                h.add(ar[i]);
            }
        }
        return c;
}
