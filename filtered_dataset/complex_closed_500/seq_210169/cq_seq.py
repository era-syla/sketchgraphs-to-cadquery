import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05575, -0.091).lineTo(0.05575, -0.091).lineTo(0.05575, -0.099).lineTo(-0.05575, -0.099).lineTo(-0.05575, -0.091).close()
solid=wp_sketch0.add(loop0).extrude(0.24716680767710178)
