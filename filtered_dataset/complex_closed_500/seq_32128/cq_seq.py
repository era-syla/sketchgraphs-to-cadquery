import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-2.4384, 1.04775).lineTo(-3.3528, 1.04775).lineTo(-3.3528, -1.04775).lineTo(-2.4384, -1.04775).lineTo(-2.4384, 1.04775).close()
solid=wp_sketch0.add(loop0).extrude(1.9350229058838608)
