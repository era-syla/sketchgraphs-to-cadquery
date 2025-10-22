import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03701, 0.03258).threePointArc((-0.03692, 0.03314), (-0.03717, 0.03363)).threePointArc((-0.0406, 0.03509), (-0.04409, 0.03639)).threePointArc((-0.04643, 0.03701), (-0.04882, 0.03667)).threePointArc((-0.04704, 0.03481), (-0.046, 0.03245)).threePointArc((-0.04148, 0.03089), (-0.03701, 0.03258)).close()
solid=wp_sketch0.add(loop0).extrude(-0.010879024817238002)
