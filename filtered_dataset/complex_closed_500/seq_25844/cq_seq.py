import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00159, 0.04307).lineTo(-0.00159, 0.003).lineTo(0.00159, 0.003).lineTo(0.00159, 0.04307).threePointArc((0.00117, 0.04506), (-0.0, 0.04672)).threePointArc((-0.00117, 0.04506), (-0.00159, 0.04307)).close()
solid=wp_sketch0.add(loop0).extrude(0.08265335669005708)
