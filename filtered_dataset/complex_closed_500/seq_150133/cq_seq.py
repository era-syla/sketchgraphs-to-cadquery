import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0465, 0.0).lineTo(-0.0435, 0.0).lineTo(-0.0435, 0.026).lineTo(-0.0465, 0.026).lineTo(-0.0465, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.006105643858232836)
