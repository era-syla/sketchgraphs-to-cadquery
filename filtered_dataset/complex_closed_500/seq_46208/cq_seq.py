import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04395, 0.051).lineTo(-0.01673, 0.051).lineTo(-0.00896, 0.01561).threePointArc((-0.01163, 0.01374), (-0.01392, 0.01141)).lineTo(-0.04165, 0.02939).threePointArc((-0.04419, 0.03176), (-0.04577, 0.03486)).lineTo(-0.04873, 0.04454).threePointArc((-0.04797, 0.04897), (-0.04395, 0.051)).close()
solid=wp_sketch0.add(loop0).extrude(-0.07521575000319881)
