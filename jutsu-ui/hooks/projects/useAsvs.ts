import { AsvsCategory } from "@/models/projects";
import asvsService from "@/services/projects/AsvsService";
import { useQuery } from "react-query";

const useAsvs = () => {
  return useQuery<AsvsCategory[], Error>(["asvs"], () =>
    asvsService.getCategories()
  );
};

export default useAsvs;
