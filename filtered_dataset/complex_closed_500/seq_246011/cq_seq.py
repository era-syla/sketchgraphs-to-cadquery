import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02708, -0.02307).threePointArc((-0.0175, -0.01393), (-0.02708, -0.00479)).lineTo(-0.02708, -0.02307).close()
solid=wp_sketch0.add(loop0).extrude(0.022962468457047854)
