import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.11744, 0.07015).lineTo(-0.11744, 0.07015).lineTo(-0.11744, -0.07015).lineTo(0.11744, -0.07015).lineTo(0.11744, 0.07015).close()
solid=wp_sketch0.add(loop0).extrude(0.4820546820588493)
