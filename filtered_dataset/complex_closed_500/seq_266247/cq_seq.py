import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.07603, -0.04623).threePointArc((0.07908, -0.0644), (0.09677, -0.0695)).threePointArc((0.09347, -0.05156), (0.07603, -0.04623)).close()
solid=wp_sketch0.add(loop0).extrude(0.018224167312006108)
