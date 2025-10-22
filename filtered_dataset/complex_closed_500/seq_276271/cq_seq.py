import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01215, 0.07073).lineTo(-0.01215, 0.07073).threePointArc((-0.0178, 0.07307), (-0.02015, 0.07873)).lineTo(-0.02015, 0.09272).lineTo(0.02015, 0.09272).lineTo(0.02015, 0.07873).threePointArc((0.0178, 0.07307), (0.01215, 0.07073)).close()
solid=wp_sketch0.add(loop0).extrude(0.10110321280469711)
