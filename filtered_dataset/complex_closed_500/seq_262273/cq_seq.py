import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(33.22058, -57.91025).lineTo(-16.77942, -57.91025).lineTo(-16.77942, -38.91025).lineTo(33.22058, -38.91025).lineTo(33.22058, -57.91025).close()
solid=wp_sketch0.add(loop0).extrude(126.94992660866325)
