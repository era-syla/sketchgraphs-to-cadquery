import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.44131, -0.42661).lineTo(-0.05869, -0.42661).lineTo(-0.05869, 0.04376).lineTo(0.44131, 0.04376).lineTo(0.44131, -0.42661).close()
solid=wp_sketch0.add(loop0).extrude(-0.6589508027386649)
