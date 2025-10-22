import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.0).lineTo(-0.072, 0.0).lineTo(-0.072, 0.021).threePointArc((-0.07112, 0.02312), (-0.069, 0.024)).lineTo(-0.023, 0.024).threePointArc((-0.02088, 0.02312), (-0.02, 0.021)).lineTo(-0.02, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.12802264276983566)
