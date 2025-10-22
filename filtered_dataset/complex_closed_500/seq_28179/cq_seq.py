import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0172).threePointArc((-0.0172, -0.0), (-0.0, -0.0172)).lineTo(0.0, 0.0172).close()
solid=wp_sketch0.add(loop0).extrude(0.07979072796701506)
