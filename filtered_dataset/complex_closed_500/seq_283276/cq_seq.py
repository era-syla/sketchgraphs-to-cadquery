import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00691, -0.00098).threePointArc((0.00941, 0.00152), (0.00691, 0.00402)).lineTo(0.00093, 0.00402).threePointArc((-0.00157, 0.00152), (0.00093, -0.00098)).lineTo(0.00691, -0.00098).close()
solid=wp_sketch0.add(loop0).extrude(0.008872512203619535)
