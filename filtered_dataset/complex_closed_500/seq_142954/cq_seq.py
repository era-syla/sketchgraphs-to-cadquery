import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.162, 0.1).lineTo(-0.002, 0.1).lineTo(-0.002, 0.095).lineTo(-0.162, 0.095).lineTo(-0.162, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(0.05791353014197874)
