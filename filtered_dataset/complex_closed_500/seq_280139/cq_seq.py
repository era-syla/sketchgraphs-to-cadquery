import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00311, -0.01099).lineTo(0.00447, -0.01432).lineTo(0.00682, -0.01336).lineTo(0.00547, -0.01003).lineTo(0.00311, -0.01099).close()
solid=wp_sketch0.add(loop0).extrude(-0.011406599218350678)
