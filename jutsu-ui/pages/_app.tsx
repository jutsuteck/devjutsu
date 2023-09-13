import type { AppProps } from "next/app";
import { QueryClient, QueryClientProvider } from "react-query";
import { Questrial } from "next/font/google";

import "@/styles/globals.css";
import { AuthProvider } from "@/contexts/AuthProvider";

const queryClient = new QueryClient();

const questrial = Questrial({ subsets: ["latin"], weight: ["400"] });

const App = ({ Component, pageProps }: AppProps) => {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <main className={`${questrial.className} tracking-wider`}>
          <Component {...pageProps} />
        </main>
      </AuthProvider>
    </QueryClientProvider>
  );
};

export default App;
