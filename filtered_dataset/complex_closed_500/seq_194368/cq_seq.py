import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06997, 0.03575).lineTo(-0.08624, 0.06575).threePointArc((-0.08725, 0.07542), (-0.08114, 0.08297)).lineTo(-0.02532, 0.11325).threePointArc((-0.01565, 0.11426), (-0.0081, 0.10814)).lineTo(0.00818, 0.07814).lineTo(-0.06997, 0.03575).close()
solid=wp_sketch0.add(loop0).extrude(-0.2168949064189748)
