import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00932, 0.00682).lineTo(-0.02678, 0.00682).lineTo(-0.02678, 0.02429).lineTo(-0.00932, 0.02429).lineTo(-0.00932, 0.00682).close()
solid=wp_sketch0.add(loop0).extrude(0.038890989226379846)
