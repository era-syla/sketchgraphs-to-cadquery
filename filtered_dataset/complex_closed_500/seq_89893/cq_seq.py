import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.27, 0.0).lineTo(-0.2764, 0.00722).threePointArc((-0.27768, 0.00817), (-0.27924, 0.0085)).lineTo(-0.28777, 0.0085).threePointArc((-0.28937, 0.00815), (-0.29067, 0.00716)).lineTo(-0.297, -0.0003).lineTo(-0.29989, -0.0003).lineTo(-0.29205, 0.00894).threePointArc((-0.29034, 0.01024), (-0.28824, 0.0107)).lineTo(-0.27879, 0.0107).threePointArc((-0.27674, 0.01026), (-0.27505, 0.00902)).lineTo(-0.26706, -0.0).lineTo(-0.27, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.039482130911733374)
