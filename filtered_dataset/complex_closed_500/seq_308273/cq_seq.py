import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03342, 0.02034).lineTo(0.01738, 0.02034).lineTo(0.01738, -0.02411).lineTo(-0.03342, -0.02411).lineTo(-0.03342, 0.02034).close()
solid=wp_sketch0.add(loop0).extrude(-0.11926653569983123)
