import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.16842, 0.14).lineTo(0.19151, 0.1).lineTo(0.19151, -0.04).lineTo(0.16842, -0.08).lineTo(0.11415, -0.08).lineTo(0.08817, -0.035).threePointArc((0.07719, -0.02402), (0.06219, -0.02)).lineTo(-0.00849, -0.02).lineTo(-0.00849, 0.06).lineTo(0.01151, 0.06).threePointArc((0.02651, 0.06402), (0.03749, 0.075)).lineTo(0.07502, 0.14).lineTo(0.16842, 0.14).close()
solid=wp_sketch0.add(loop0).extrude(-0.4654045137184329)
