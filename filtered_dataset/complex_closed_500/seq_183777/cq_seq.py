import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0076, 0.013).lineTo(0.0026, 0.013).lineTo(0.0026, 0.009).lineTo(-0.0076, 0.009).lineTo(-0.0076, 0.013).close()
solid=wp_sketch0.add(loop0).extrude(0.004266802099501526)
