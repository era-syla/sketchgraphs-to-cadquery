import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.02033).lineTo(0.0, -0.01804).lineTo(-0.00185, -0.01804).lineTo(-0.00733, -0.02033).lineTo(0.0, -0.02033).close()
solid=wp_sketch0.add(loop0).extrude(0.02164407235292066)
