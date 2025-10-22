import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05978, 0.0).lineTo(-0.04708, 0.0).lineTo(-0.04708, 0.0254).lineTo(-0.05978, 0.0254).lineTo(-0.05978, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.02520150546957032)
