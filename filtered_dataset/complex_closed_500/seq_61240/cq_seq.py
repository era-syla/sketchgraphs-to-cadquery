import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.12, 0.01225).lineTo(-0.12, 0.01225).lineTo(-0.12, -0.21275).lineTo(0.12, -0.21275).lineTo(0.12, 0.01225).close()
solid=wp_sketch0.add(loop0).extrude(0.25615345633384334)
