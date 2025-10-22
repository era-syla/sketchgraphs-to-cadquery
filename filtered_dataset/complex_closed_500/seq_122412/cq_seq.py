import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.075, -0.08).lineTo(-0.075, -0.08).lineTo(-0.075, 0.08).lineTo(0.075, 0.08).lineTo(0.075, -0.08).close()
solid=wp_sketch0.add(loop0).extrude(-0.3272448453857181)
