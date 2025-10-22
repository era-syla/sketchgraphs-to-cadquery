import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.04191).lineTo(0.0, -0.03614).threePointArc((-0.04102, 0.00288), (0.0, 0.04191)).close()
solid=wp_sketch0.add(loop0).extrude(-0.1246697685993481)
