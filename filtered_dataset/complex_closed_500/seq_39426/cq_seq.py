import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.075, 0.075).lineTo(0.075, 0.075).lineTo(0.075, -0.075).lineTo(-0.075, -0.075).lineTo(-0.075, 0.075).close()
solid=wp_sketch0.add(loop0).extrude(-0.06821942025928211)
