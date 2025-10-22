import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03429, 0.04319).lineTo(0.03429, 0.04319).lineTo(0.03429, -0.01357).lineTo(-0.03429, -0.01357).lineTo(-0.03429, 0.04319).close()
solid=wp_sketch0.add(loop0).extrude(-0.10640137528105974)
