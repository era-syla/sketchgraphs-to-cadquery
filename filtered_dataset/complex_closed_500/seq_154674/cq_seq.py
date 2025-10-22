import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.137, 0.334).lineTo(-1.46, 0.334).lineTo(-1.46, -0.334).lineTo(-2.137, -0.334).lineTo(-2.137, 0.334).close()
solid=wp_sketch0.add(loop0).extrude(0.5939791335025325)
