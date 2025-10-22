import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.08093, 0.12622).lineTo(-0.08474, 0.12622).lineTo(-0.08474, 0.1294).lineTo(-0.08664, 0.1294).lineTo(-0.08664, 0.12495).lineTo(-0.08093, 0.12495).lineTo(-0.08093, 0.12622).close()
solid=wp_sketch0.add(loop0).extrude(0.008173669434852208)
