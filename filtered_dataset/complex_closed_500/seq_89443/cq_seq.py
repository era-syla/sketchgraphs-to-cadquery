import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03048, 0.06985).threePointArc((0.0, 0.03937), (0.03048, 0.06985)).lineTo(0.04064, 0.06985).threePointArc((-0.0, 0.02921), (-0.04064, 0.06985)).lineTo(-0.03048, 0.06985).close()
solid=wp_sketch0.add(loop0).extrude(0.037385319073162455)
