import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05196, -0.03921).lineTo(-0.03747, -0.03921).lineTo(-0.03747, -0.04524).lineTo(-0.05196, -0.04524).lineTo(-0.05196, -0.03921).close()
solid=wp_sketch0.add(loop0).extrude(-0.028479305015852288)
