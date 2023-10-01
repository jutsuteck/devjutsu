import React, { ReactNode } from "react";

interface Columns {
  small?: number;
  medium?: number;
  large?: number;
}

interface Gap {
  horizontal: number;
  vertical: number;
}

interface MasonryProps {
  columns?: Columns;
  gap?: Gap;
  children: ReactNode;
}

const Masonry: React.FC<MasonryProps> = ({
  columns = { small: 2, medium: 3, large: 6 },
  gap = { horizontal: 10, vertical: 10 },
  children,
}) => {
  return (
    <div className={`relative`}>
      {/* Media Queries for Responsive Columns */}
      <style>{`
        .masonry {
          column-count: ${columns.large};
          column-gap: ${gap.horizontal}px;
        }
        @media screen and (max-width: 480px) {
          .masonry { column-count: ${columns.small}; }
        }
        @media screen and (min-width: 481px) and (max-width: 1024px) {
          .masonry { column-count: ${columns.medium}; }
        }
        .masonry > div {
          display: inline-block;
          width: 100%;
          box-sizing: border-box;
          margin-bottom: ${gap.vertical}px;
        }
      `}</style>

      <div className="masonry">
        {React.Children.map(children, (child) => (
          <div>{child}</div>
        ))}
      </div>
    </div>
  );
};

export default Masonry;
