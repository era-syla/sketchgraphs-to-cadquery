import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0126, -0.02591).lineTo(-0.02348, -0.02591).lineTo(-0.02348, 0.02626).lineTo(0.0126, 0.02626).lineTo(0.0126, -0.02591).close()
solid=wp_sketch0.add(loop0).extrude(-0.025764544286210157)
