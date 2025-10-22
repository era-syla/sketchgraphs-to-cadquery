import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03211, 0.0243).threePointArc((0.03093, 0.01754), (0.03752, 0.01944)).threePointArc((0.03343, 0.02032), (0.03211, 0.0243)).close()
solid=wp_sketch0.add(loop0).extrude(-0.012704314604927054)
