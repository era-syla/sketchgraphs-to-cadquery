import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-43.93225, 0.0).lineTo(-43.32265, 0.0).lineTo(-43.32265, 2.02997).lineTo(-43.93225, 2.02997).lineTo(-43.93225, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(5.333647399008721)
