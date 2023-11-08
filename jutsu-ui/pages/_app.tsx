import type { AppProps } from "next/app";
import { QueryClient, QueryClientProvider } from "react-query";
import { Manrope } from "next/font/google";

import "@/styles/globals.css";
import { AuthProvider } from "@/contexts/AuthProvider";

const queryClient = new QueryClient();

const fontFamily = Manrope({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
});

const App = ({ Component, pageProps }: AppProps) => {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <main className={`${fontFamily.className} tracking-wider`}>
          <Component {...pageProps} />
        </main>
      </AuthProvider>
    </QueryClientProvider>
  );
};

export default App;
