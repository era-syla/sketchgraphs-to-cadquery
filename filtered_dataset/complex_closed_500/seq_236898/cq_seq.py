import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.4384, -0.63935).lineTo(-1.23825, -0.63935).lineTo(-1.23825, -0.85267).lineTo(-2.4384, -0.85267).lineTo(-2.4384, -0.63935).close()
solid=wp_sketch0.add(loop0).extrude(-1.2022276378735848)
