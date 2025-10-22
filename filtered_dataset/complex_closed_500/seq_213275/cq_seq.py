import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0634, 0.05493).lineTo(0.0634, 0.05493).lineTo(0.0634, -0.05493).lineTo(-0.0634, -0.05493).lineTo(-0.0634, 0.05493).close()
solid=wp_sketch0.add(loop0).extrude(0.0854440007458471)
