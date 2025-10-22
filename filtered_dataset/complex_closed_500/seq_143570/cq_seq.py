import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.43892, -0.45258).lineTo(4.79319, -4.67684).lineTo(5.60636, -3.83865).lineTo(4.36668, -2.63598).lineTo(4.24793, -2.75838).lineTo(2.3246, -0.89248).lineTo(2.44335, -0.77007).lineTo(0.91527, 0.71238).lineTo(0.43892, -0.45258).close()
solid=wp_sketch0.add(loop0).extrude(9.241652454929138)
