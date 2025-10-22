import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.004, 0.04).lineTo(-0.004, 0.04).lineTo(-0.004, -0.04).lineTo(0.004, -0.04).lineTo(0.004, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.04853846148459894)
