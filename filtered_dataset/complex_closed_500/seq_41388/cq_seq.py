import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.5554, -1.33).lineTo(-0.6354, -1.33).lineTo(-0.6354, -1.39).lineTo(-0.5554, -1.39).lineTo(-0.5554, -1.33).close()
solid=wp_sketch0.add(loop0).extrude(-0.19567950522542976)
