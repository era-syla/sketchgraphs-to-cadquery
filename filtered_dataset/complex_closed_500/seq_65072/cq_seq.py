import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04, -0.8).lineTo(3.21, -0.8).lineTo(3.21, 0.0).lineTo(-0.04, 0.0).lineTo(-0.04, -0.8).close()
solid=wp_sketch0.add(loop0).extrude(-9.72508782449018)
